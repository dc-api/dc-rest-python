# ApplicationRoleConnectionsMetadataItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**key** | **str** |  | 
**name** | **str** |  | 
**name_localizations** | **Dict[str, Optional[str]]** |  | [optional] 
**description** | **str** |  | 
**description_localizations** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from dc_rest.models.application_role_connections_metadata_item_request import ApplicationRoleConnectionsMetadataItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRoleConnectionsMetadataItemRequest from a JSON string
application_role_connections_metadata_item_request_instance = ApplicationRoleConnectionsMetadataItemRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationRoleConnectionsMetadataItemRequest.to_json())

# convert the object into a dict
application_role_connections_metadata_item_request_dict = application_role_connections_metadata_item_request_instance.to_dict()
# create an instance of ApplicationRoleConnectionsMetadataItemRequest from a dict
application_role_connections_metadata_item_request_from_dict = ApplicationRoleConnectionsMetadataItemRequest.from_dict(application_role_connections_metadata_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


