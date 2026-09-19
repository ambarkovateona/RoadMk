from database import engine, Base
from models import RoadReport

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")