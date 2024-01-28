import logging
import os
import sys

import ijson
from sqlalchemy.exc import SQLAlchemyError

from app.database import get_db
from app.tenants import TenantSchema, TenantModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def process_tenant(item, db):
    validated_data = TenantSchema(**item)
    new_tenant = TenantModel(
        id=validated_data.id,
        number=validated_data.number,
        info=validated_data.info
    )
    db.add(new_tenant)


def db_commit(db, batch_counter):
    try:
        db.commit()
        logging.info(f'INSERTED {batch_counter} tenants')
        db.expunge_all()  # Clear session to free memory
        return 0
    except SQLAlchemyError as db_err:
        logging.error(f'Database commit error: {db_err}')
        db.rollback()
        return batch_counter


def read_and_validate_params():
    data_filename = os.getenv('data_filename')
    batch_size = os.getenv('import_batch_size')

    batch_size = int(batch_size) if batch_size is not None else batch_size

    if not data_filename:
        sys.exit(0)

    if not data_filename.endswith(".json"):
        raise ValueError("Import script supports only JSON files.")

    return data_filename, batch_size


def main():
    data_filename, batch_size = read_and_validate_params()

    with open(data_filename, "rb") as f:
        batch_counter = 0
        db = next(get_db())
        for item in ijson.items(f, 'item'):
            process_tenant(item, db)
            if batch_size:
                batch_counter += 1
                if batch_counter >= batch_size:
                    batch_counter = db_commit(db, batch_counter)
            else:
                db_commit(db, 1)
        if batch_counter:
            db_commit(db, batch_counter)


if __name__ == '__main__':
    main()
