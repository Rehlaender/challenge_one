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
    
def update_incident(payload): 
    try:  
        incident = PagerDutyAPISession.rput(
                f"/incidents/{payload['id']}",
                headers={"From": payload['from']},
                json=payload['form']
            )
        return incident
    
    except PDClientError as e:
        print(e.msg)
        return e.response.text
    
# Get a status of all incidents associated with a service 
# (total incidents by status, percentage of incidents by status)
def get_service_incident_status(service_id):
    try: 
        incidents = get_all_incidents_by_service(service_id)
        
        awesomeDashboard = {
            'resolved': [],
            'acknowledged': [],
            'triggered': [],
        }
        
        incidentsByStatus = dict()
        incidentsByPercentage = dict()
        totalIncidents = len(incidents)

        # Iterate over all the incidents and separate by status
        for incident in incidents:
            print({'status': incident['status'], 'id': incident['id']})
            awesomeDashboard[incident['status']].append(incident)
        
        # Iterate Dashboard and count percentage and total
        for key, status in awesomeDashboard.items(): 
            print(key, totalIncidents, len(status), 'jijiji')
            incidentsByPercentage[key] = (len(status) / totalIncidents) * 100
            incidentsByStatus[key] = len(status)
        return {
            "dashboard": awesomeDashboard, 
            "incidentByStatus": incidentsByStatus,
            "percentages": incidentsByPercentage,
            "totalIncidents": totalIncidents
        }

    except PDClientError as e:
        print(e.msg)
        return e.response.text