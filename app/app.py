from flask import Flask, request, jsonify
from query_generator import generate_sql_query
from db_connection import execute_query

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query_db():
    """Handle incoming natural language queries"""
    try:
        data = request.json
        user_query = data.get("query")

        if not user_query:
            return jsonify({"error": "No query provided"}), 400

        # Convert NL to SQL
        sql_query = generate_sql_query(user_query)

        # Execute SQL
        results = execute_query(sql_query)

        return jsonify({"sql_query": sql_query, "results": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
