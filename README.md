[![PyPI version](https://badge.fury.io/py/pycherwell.svg)](https://badge.fury.io/py/pycherwell)
![app](https://github.com/greenpau/pycherwell/workflows/app/badge.svg?branch=master)

# Cherwell API Client

![Cherwell API](https://raw.githubusercontent.com/greenpau/pycherwell/master/logo.png "Cherwell API")

## Getting Started

### Installation

If necessary, upgrade `pip`:

```bash
python3 -m pip install --upgrade pip setuptools wheel twine
```

Install with PyPI:

```bash
pip3 install pycherwell --user
```

Install from source:

```bash
git clone https://github.com/greenpau/pycherwell.git
cd pycherwell
pip3 install -r requirements.txt --user
python3 setup.py install --user --record installed_files.txt
```

If necessary, uninstall `pycherwell`:

```bash
pip3 uninstall pycherwell
cat installed_files.txt | xargs sudo rm -rf
```

### Configuration

LDAP Configuration file: `~/.cherwell/config`:

```toml
[default]
client_id = "5d4f6f1b-f0de-4442-8791-4582816b04de"
auth_mode = "LDAP"
username = "MYDOMAIN\myappuser"
password = "xxxxxx"
host = "myapp.cherwellondemand.com"
port = "443"
protocol = "https"
```

LOCAL configuration file: `~/.cherwell/config`:

```toml
[default]
client_id = "5d4f6f1b-f0de-4442-8791-4582816b04de"
auth_mode = "Internal"
username = "Cherwell\myappuser"
password = "xxxxxx"
host = "myapp.cherwellondemand.com"
port = "443"
protocol = "https"
```

### Testing

The following command checks whether the services is available:

```bash
$ cherwell-client --get-service-info --debug
```

The expected output is:

```json
{
    "service_info": {
        "api_version": "9.3.2",
        "csm_culture": "en-US",
        "csm_version": "9.3.2",
        "system_date_time": "2019-11-18 18:14:42.510452+00:00"
    }
}
```

## Usage Instructions

### Business Objects

The following commands fetches business object summaries. It is a reference to
the IDs for business objects themselves, their fields, states, etc.

```bash
cherwell-client --get-business-object-summaries > business-object-summaries.json
{
    "business_object_summaries": [
        {
            "bus_ob_id": "fe838f7d1a8d4a748940dba7be76995c",
            "display_name": "Incident",
            "first_rec_id_field": "3910bef5813c421a92e4a68eea109a95",
            "group": false,
            "group_summaries": [],
            "lookup": false,
            "major": true,
            "name": "Incident",
            "rec_id_fields": "f5e8c54b647f48ad81e720132624001e",
            "state_field_id": "cb62a991a2cb4fd98cab26c3519b2d92",
            "states": "Pending,Closed,Reopened,New,In Progress,Resolved,Assigned",
            "supporting": false
        }
    ]
}
```

By default, the tool stores the returned business objects in
`~/.cherwell/business_object.json`. Subsequent requests return the content of that file,
unless the invocation includes `--rebase` argument.

```bash
cherwell-client --get-business-object-summaries --rebase
```

### Incidents

The following command returns incidents owned by "Application Development" team:

```bash
cherwell-client --get-incidents --debug --search-condition "Owned By Team:eq:Application Development"
```

The following command returns CSV list containing incident ID, type and status
of all "Pending" items for "Application Development" team:

```bash
cherwell-client --get-incidents \
  --search-condition "Status:eq:Pending" \
  --search-condition "Owned By Team:eq:Application Development" \
  --search-field "IncidentID" --search-field "IncidentType" \
  --search-field "Status" --format csv
```

The following command returns CSV list of unresolved and not closed items
for "Application Development" team:

```bash
cherwell-client --get-incidents \
  --search-condition "Owned By Team:eq:Application Development" \
  --search-condition "Status:eq:Pending" \
  --search-condition "Status:eq:Assigned" \
  --search-condition "Status:eq:In Progress" \
  --search-condition "Status:eq:New" \
  --search-field "IncidentID" --search-field "IncidentType" --search-field "Status" \
  --search-field "Service" --search-field "Category"  --search-field "Subcategory" \
  --search-field "Customer Display Name" \
  --search-field "Owned By" \
  --search-field "Created Date Time" \
  --search-field "Short Description" \
  --format csv
```

The following command is a variation of the one above:

```bash
cherwell-client --get-incidents \
  --search-condition "Service:eq:Application Support" \
  --search-condition "Status:eq:Pending" \
  --search-condition "Status:eq:Assigned" \
  --search-condition "Status:eq:In Progress" \
  --search-condition "Status:eq:New" \
  --search-field "IncidentID" --search-field "IncidentType" --search-field "Status" \
  --search-field "Service" --search-field "Category"  --search-field "Subcategory" \
  --search-field "Customer Display Name" \
  --search-field "Owned By" \
  --search-field "Owned By Team" \
  --search-field "Created Date Time" \
  --search-field "Short Description" \
  --format csv
```

The following command returns information about Cherwell Incident 1234567:

```bash
cherwell-client --get-incident 1234567 --debug --format yaml
```

### Teams

Get the list of teams:

```bash
cherwell-client --get-teams --format text
```
