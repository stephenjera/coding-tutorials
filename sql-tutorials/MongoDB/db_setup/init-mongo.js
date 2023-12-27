// Check if database exists
if (db.getMongo().getDBNames().indexOf("restapi") == -1) {
    // Create database
    db = db.getSiblingDB("restapi");
    print("Created database restapi");
  } else {
    // Use existing database
    db = db.getSiblingDB("restapi");
    print("Using existing database restapi");
  }
  
  db.createUser({
    user: "restapi_user",
    pwd: "password",
    roles: [{ role: "readWrite", db: "restapi" }]
  });
  
  // Check if collection exists
  if (db.getCollectionNames().indexOf("users") == -1) {
    // Create collection
    db.createCollection("users");
    print("Created collection users");
    // Insert documents
    db.users.insertMany([
      {
        name: "John",
        age: 30,
        username: "john30",
      },
      {
        name: "Jane",
        age: 28,
        username: "jane28",
      },
      {
        name: "Bob",
        age: 40,
        username: "bobby40",
      },
      {
        name: "Penny",
        age: 50,
        username: "penny50",
      },
    ]);
    print("Inserted documents into collection users");
    
  } else {
    print("Collection users already exists");
  }
  