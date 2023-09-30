from pdpyras import APISession, PDClientError, EventsAPISession
from os import environ as ENV

PagerDutyAPISession = APISession(ENV.get("PAGERDUTY_REST_API_KEY"))

def get_all_services():
    print("Get ALL Services.")
    try:
        services = PagerDutyAPISession.rget(
            "/services",
        )
        return services
    except PDClientError as e:
        print(e.msg)
        return e.response.text

def get_all_incidents():
    print("Get ALL Incidents.")
    try:
        incidents = PagerDutyAPISession.rget(
            "/incidents",
        )
        return incidents
    except PDClientError as e:
        print(e.msg)
        return e.response.text
    
def get_all_incidents_by_service(service_id):
    try:
        incidents_by_service_id = PagerDutyAPISession.rget(
            f"/incidents",
            params={"service_ids[]": ["P8A9YNH"]}
        )

        return incidents_by_service_id
    except PDClientError as e:
        print(e.msg)
        return e.response.text

def get_all_status_per_incident(incident_id):
    try:
        incident = PagerDutyAPISession.rget(
            f"/incidents/{incident_id}",
        )
        print(incident['status'])
        return incident
    
    except PDClientError as e:
        print(e.msg)
        return e.response.text

def creat_incident(): 
    try:  
        incident = PagerDutyAPISession.rpost(
                f"/incidents",
                json={
                    "incident": {
                        "type": "incident",
                        "title": "The server is on fire.",
                        "service": {
                            "id": "PWIXJZS",
                            "type": "service_reference"
                        },
                        "priority": {
                            "id": "P53ZZH5",
                            "type": "priority_reference"
                        },
                        "urgency": "high",
                        "incident_key": "baf7cf21b1da41b4b0221008339ff357",
                        "body": {
                            "type": "incident_body",
                            "details": "A disk is getting full on this machine. You should investigate what is causing the disk to fill, and ensure that there is an automated process in place for ensuring data is rotated (eg. logs should have logrotate around them). If data is expected to stay on this disk forever, you should start planning to scale up to a larger disk."
                        },
                        "escalation_policy": {
                            "id": "PT20YPA",
                            "type": "escalation_policy_reference"
                        }
                    }
                }
            )
        return incident
    
    except PDClientError as e:
        print(e.msg)
        return e.response.text