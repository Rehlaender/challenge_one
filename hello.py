from flask import Flask

app = Flask(__name__)

@app.route('/products', methods=['POST'])
def create_product():
    # Handle product creation logic
    return "Product created successfully"

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    # Handle product retrieval logic
    return f"Product ID: {product_id}"

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    # Handle product update logic
    return f"Product ID: {product_id} updated successfully"

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Handle product deletion logic
    return f"Product ID: {product_id} deleted successfully"

if __name__ == '__main__':
    app.run()
