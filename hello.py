from flask import Flask, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/services', methods=['GET'])
    def get_services():
        import api
        return api.get_all_services()
    
    @app.route('/incidents-by-service/<service_id>', methods=['GET'])
    def get_incidents(service_id):
        import api
        return api.get_all_incidents_by_service(service_id)

    @app.route('/status-of-incident/<incident_id>', methods=['GET'])
    def get_all_status_per_incident(incident_id):
        print(incident_id)
        import api
        return api.get_all_status_per_incident(incident_id)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)