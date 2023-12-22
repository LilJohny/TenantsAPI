# TenantsAPI

## Overview
TenantsAPI is a tool designed using FastAPI to streamline tenant management processes.

## Core Functionalities

### Routes:
1. **List Tenants**
   - This route fetches and displays a  list of all available tenants, including details such as tenant ID, number, and additional information.

2. **Get Tenant by ID**
- This functionality allows for retrieving a tenant's details (ID, number, and info) based on their unique identifier(ID).

3. **Create New Tenant**
- This endpoint facilitates the creation of a new tenant record. The provided information and ID are processed, with an auto-generated number prefixed to the ID before it's stored in the database.
- Note: This feature is my addition, implemented to simplify testing procedures.

### Data Import Script: `import_data.py`
- **Functionality**: It reads tenant data from a specified JSON file, validates the data, and writes it to the database upon validation.
- **Efficient Data Handling**: Utilizing `ijson`, the script avoids loading the entire dataset into memory, instead processing data object-by-object.
- **Environment Variables Requirement**:
- `data_filename`: Specifies the JSON file's name from which the data is read.
- `import_batch_size`: Determines the size of the tenant batch to optimize memory usage, especially useful for large JSON files.
