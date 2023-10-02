## Intreview challenge

This project is planned as a show case of connecting a flask+react project and consume and render the given Services.

### Goals

- a. Get all The services in your instance :heavy_check_mark:
- b. Get all incidents per Service :heavy_check_mark:
- c. Get all status per incident :heavy_check_mark:
- d. Create new incidents :heavy_check_mark:
- e. Change the incidents status :heavy_check_mark:
- f. Get a status of all incidents associated with a service (total incidents by status, 
- percentage of incidents by status) :heavy_check_mark:

### Required
- a. Is required the use of Flask and Python 3.10 or higher. :heavy_check_mark: 
- b. You must add unit testing to your development :x:
- c. You must use a git repository :heavy_check_mark: 

### Desirable
- a. Upload the project as a microservice (AWS, EC2, Kubernetes, Docker) :x:

## Steps to install/run

- `clone project`
- Set your API key in .env with the key `PAGERDUTY_REST_API_KEY=`
- `pip install -r requirements.txt`
- `flask --app hello run` - start dev server http://localhost:5000/

### Request

`GET /services/`

    Gets all the services 

### Request

`GET /incidents-by-service/{service_id}/`

    Gets all the incidents of an specific service

### Request

`POST /new-incident/`

    Creates a new incident

```JSON
Example payload
{
    "from": "{your_email}",
    "form": {
        "incident": {
            "type": "incident",
            "title": "{incident_title}",
            "service": {
                "id": "{service_id}",
                "type": "service_reference"
            },
            "body": {
                "type": "new incident",
                "details": "{incident_detail}"
            }
        }
    }
}
```

### Request

`PUT /update-incident-status`

    Updates an incident

```JSON
Exapmle payload
{
    "id": "{incident_id}",
    "from": "{your_email}",
    "form": {
        "incident": {
            "type": "incident_reference",
            "status": "{new_status}"
        }
    }
}
```

### Request

`GET /awesome-dashboard/{service_id}`

    Get a status of all incidents associated with a service (total incidents by status, - percentage of incidents by status)

```JSON
{
    "dashboard": {
        "acknowledged": ["array with all the acknowledged incidents"],
        "resolved": ["array with all the resolved incidents"],
        "triggered": ["array with all the triggered incidents"]
    },
    "incidentByStatus": {
        "acknowledged": "#",
        "resolved": "#",
        "triggered": "#"
    },
    "percentages": {
        "acknowledged": "%",
        "resolved": "%",
        "triggered": "%"
    },
    "totalIncidents": "#"
}
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
