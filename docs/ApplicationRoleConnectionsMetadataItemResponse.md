# ApplicationRoleConnectionsMetadataItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**key** | **str** |  | 
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**description_localizations** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dc_rest.models.application_role_connections_metadata_item_response import ApplicationRoleConnectionsMetadataItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRoleConnectionsMetadataItemResponse from a JSON string
application_role_connections_metadata_item_response_instance = ApplicationRoleConnectionsMetadataItemResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationRoleConnectionsMetadataItemResponse.to_json())

# convert the object into a dict
application_role_connections_metadata_item_response_dict = application_role_connections_metadata_item_response_instance.to_dict()
# create an instance of ApplicationRoleConnectionsMetadataItemResponse from a dict
application_role_connections_metadata_item_response_from_dict = ApplicationRoleConnectionsMetadataItemResponse.from_dict(application_role_connections_metadata_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


