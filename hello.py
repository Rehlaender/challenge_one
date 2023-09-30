from flask import Flask, request
import api

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/services', methods=['GET'])
    def get_services():
        return api.get_all_services()
    
    @app.route('/incidents-by-service/<service_id>', methods=['GET'])
    def get_incidents(service_id):
        return api.get_all_incidents_by_service(service_id)

    @app.route('/status-of-incident/<incident_id>', methods=['GET'])
    def get_all_status_per_incident(incident_id):
        print(incident_id)
        return api.get_all_status_per_incident(incident_id)

    @app.route('/new-incident', methods=['POST'])
    def create_incident():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            payload = request.json
            print(payload)
            return api.creat_incident(payload)
        else:
            return 'Content-Type not supported!'
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)