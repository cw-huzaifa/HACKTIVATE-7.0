# Maintenance & Service Cost Predictor

**Problem:** Users often underestimate long-term maintenance costs of vehicles.
**Solution:** AI-based cost predictor estimates future maintenance expenses based on car model, age, past service records, and driving behavior.


## Steps :
- Used Car 
- DataSet - supervised 
- Finetune / Vector Database
- gemini Ai model -> python -> user's data of used car ( Previous history ) 
- store response in DB

## Tech Stack :
- Python , flask, gemini sdk, vector DB ( Pinecone if any ) or finetune gemini model.


## Tasks :
- Find Datasets
- project setup ( python flask and its packages )
- get gemini api key and check AI studio ( for finetune if possible )
- Setup Pinecone vector Database also check how to create vector embeddings for free to insert into vector database and to convert user query to vector 
- Then Start integrating 