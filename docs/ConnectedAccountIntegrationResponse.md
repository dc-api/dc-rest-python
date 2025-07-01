# ConnectedAccountIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**account** | [**AccountResponse**](AccountResponse.md) |  | 
**guild** | [**ConnectedAccountGuildResponse**](ConnectedAccountGuildResponse.md) |  | 

## Example

```python
from dc_rest.models.connected_account_integration_response import ConnectedAccountIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountIntegrationResponse from a JSON string
connected_account_integration_response_instance = ConnectedAccountIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountIntegrationResponse.to_json())

# convert the object into a dict
connected_account_integration_response_dict = connected_account_integration_response_instance.to_dict()
# create an instance of ConnectedAccountIntegrationResponse from a dict
connected_account_integration_response_from_dict = ConnectedAccountIntegrationResponse.from_dict(connected_account_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


