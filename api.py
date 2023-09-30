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
            params={"service_ids[]": [service_id]}
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

def creat_incident(payload): 
    try:  
        incident = PagerDutyAPISession.rpost(
                f"/incidents",
                headers={"From": payload['from']},
                json=payload['form']
            )
        return incident
    
    except PDClientError as e:
        print(e.msg)
        return e.response.text