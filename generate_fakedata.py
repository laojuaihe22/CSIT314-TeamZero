from pymongo import MongoClient
from bson import ObjectId
import random
import json

# Initialize MongoDB client and database
client = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/?tls=true")
db = client['CSIT314']  # Use or replace 'mydatabase' with your database name

def create_user_accounts(role, prefix, count):
    user_accounts = []
    for i in range(1, count + 1):
        email = f"{prefix}{i}@example.com"
        user_account = {
            "email": email,
            "password": "1",
            "status": True
        }
        user_accounts.append(user_account)
    return user_accounts

def insert_user_accounts(user_accounts):
    accounts_collection = db['UserAccount']  # Use or replace 'userAccounts' with your collection name
    result = accounts_collection.insert_many(user_accounts)
    return result.inserted_ids

def create_user_profiles(inserted_ids, role, prefix):
    user_profiles = []
    for idx, user_id in enumerate(inserted_ids):
        user_profile = {
            "userAccountId": ObjectId(user_id),
            "name": f"{role.capitalize()} {idx + 1}",
            "role": role,
            "description": f"I am a {role}",
            "status": True
        }
        user_profiles.append(user_profile)
    return user_profiles

def insert_user_profiles(user_profiles):
    profiles_collection = db['UserProfile']  # Use or replace 'userProfiles' with your collection name
    profiles_collection.insert_many(user_profiles)

def get_user_ids_by_role(role):
    """
    Retrieve all user IDs from the userProfiles collection based on role.
    """
    profiles_collection = db['UserProfile']
    ids = [doc['userAccountId'] for doc in profiles_collection.find({"role": role}, {"_id": 0, "userAccountId": 1})]
    return ids

def create_fake_ratings(num_ratings, buyer_seller_ids, agent_ids):
    """
    Generate and insert fake ratings.
    """
    ratings_collection = db['Rating']
    ratings = []
    for _ in range(num_ratings):
        sender_id = ObjectId(random.choice(buyer_seller_ids))
        receiver_id = ObjectId(random.choice(agent_ids))
        rating = random.randint(1, 5)
        rating_data = {
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "rating": rating
        }
        ratings.append(rating_data)
    ratings_collection.insert_many(ratings)

def create_fake_reviews(num_reviews, buyer_seller_ids, agent_ids):
    """
    Generate and insert fake reviews.
    """
    reviews_collection = db['Review']
    reviews = []
    review_texts = [
        "Great service, highly recommended!",
        "Very responsive and professional.",
        "Could be better. Had to wait for responses.",
        "Excellent experience, will definitely work with again!",
        "Not what I expected, quite disappointing."
    ]
    for _ in range(num_reviews):
        sender_id = ObjectId(random.choice(buyer_seller_ids))
        receiver_id = ObjectId(random.choice(agent_ids))
        review = random.choice(review_texts)  # Pick a random review text from the list
        review_data = {
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "review": review
        }
        reviews.append(review_data)
    reviews_collection.insert_many(reviews)

def create_fake_property_listings(num_listings, agent_ids, seller_ids):
    """
    Generate and insert fake property listings with diverse types and regions.
    Ensures unique addresses for each property.
    """
    listings_collection = db['propertyListing']
    properties = []
    property_types = ['HDB', 'Condo', 'Landed']
    regions = ['North', 'South', 'East', 'West', 'Central']
    street_names = ['Main St', 'Ocean Blvd', 'Pine Tree Ln', 'Maple Ave', 'Cedar Rd']

    for i in range(num_listings):
        property_type = random.choice(property_types)
        region = random.choice(regions)
        street_name = random.choice(street_names)
        address = f"{100 + i} {street_name}"  # Ensuring unique address by incrementing number

        property_data = {
            "agentID": ObjectId(random.choice(agent_ids)),
            "sellerID": ObjectId(random.choice(seller_ids)),
            "propertyName": f"{property_type} Property",
            "address": address,
            "region": region,
            "price": random.randint(100000, 500000),
            "type": property_type,
            "description": f"Spacious {property_type.lower()} with beautiful views",
            "bedroom": random.randint(1, 5),
            "bathroom": random.randint(1, 3),
            "status": random.choice(["sold", "unsold"]),
            "totalviews": random.randint(0, 1000),
            "shortlisted": 0
        }
        properties.append(property_data)

    listings_collection.insert_many(properties)
    print(f"{num_listings} property listings have been generated and inserted.")



def main():
    # # Buyers
    # buyer_accounts = create_user_accounts("buyer", "buyer", 30)
    # buyer_ids = insert_user_accounts(buyer_accounts)
    # buyer_profiles = create_user_profiles(buyer_ids, "buyer", "buyer")
    # insert_user_profiles(buyer_profiles)

    # # Real Estate Agents
    # rea_accounts = create_user_accounts("rea", "agent", 30)
    # rea_ids = insert_user_accounts(rea_accounts)
    # rea_profiles = create_user_profiles(rea_ids, "rea", "agent")
    # insert_user_profiles(rea_profiles)

    # # Sellers
    # seller_accounts = create_user_accounts("seller", "seller", 30)
    # seller_ids = insert_user_accounts(seller_accounts)
    # seller_profiles = create_user_profiles(seller_ids, "seller", "seller")
    # insert_user_profiles(seller_profiles)

    # # Admins
    # admin_accounts = create_user_accounts("admin", "admin", 10)
    # admin_ids = insert_user_accounts(admin_accounts)
    # admin_profiles = create_user_profiles(admin_ids, "admin", "admin")
    # insert_user_profiles(admin_profiles)

    # Get agent and seller IDs
    agent_ids = get_user_ids_by_role('rea')
    seller_ids = get_user_ids_by_role('seller')

    # Generate property listings
    create_fake_property_listings(100, agent_ids, seller_ids)

    # print("All data has been successfully generated and inserted into MongoDB.")

    # Generating Ratings & Reviews
    # Get buyer and seller IDs combined
    # buyer_ids = get_user_ids_by_role('buyer')
    # seller_ids = get_user_ids_by_role('seller')
    # buyer_seller_ids = buyer_ids + seller_ids

    # # Get real estate agent IDs
    # agent_ids = get_user_ids_by_role('rea')

    # # Generate ratings
    # # create_fake_ratings(200, buyer_seller_ids, agent_ids)
    # create_fake_reviews(200, buyer_seller_ids, agent_ids)

    # print("Reviews have been generated and inserted into the database.")


if __name__ == "__main__":
    main()
