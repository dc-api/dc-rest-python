# AuditLogObjectChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**new_value** | **object** |  | [optional] 
**old_value** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.audit_log_object_change_response import AuditLogObjectChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogObjectChangeResponse from a JSON string
audit_log_object_change_response_instance = AuditLogObjectChangeResponse.from_json(json)
# print the JSON string representation of the object
print(AuditLogObjectChangeResponse.to_json())

# convert the object into a dict
audit_log_object_change_response_dict = audit_log_object_change_response_instance.to_dict()
# create an instance of AuditLogObjectChangeResponse from a dict
audit_log_object_change_response_from_dict = AuditLogObjectChangeResponse.from_dict(audit_log_object_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


