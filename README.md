pip install -r requirements.txt

Endpoints
GET /api/documents/: Get all documents
POST /api/documents/: Create a new document
GET /api/documents/<id>/: Get a single document by ID
PUT /api/documents/<id>/: Update a document by ID
DELETE /api/documents/<id>/: Delete a document by ID
POST /api/auth/: Authenticate and obtain a token


To run test:
python manage.py test


Docker:

docker build -t document-repository .
docker run -p 8000:8000 document-repository



