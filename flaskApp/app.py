from flask import Flask,request

app=Flask(__name__)

stores=[{
  "name":"My Store",
  "items":[{
      "name":"chair",
      "price":15.99
  }]
}
]
# route decorator
@app.get("/store")
def get_store():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data=request.get_json()
    new_store={"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item={"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404