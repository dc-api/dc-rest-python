# ConnectedAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**type** | **str** |  | 
**friend_sync** | **bool** |  | 
**integrations** | [**List[ConnectedAccountIntegrationResponse]**](ConnectedAccountIntegrationResponse.md) |  | [optional] 
**show_activity** | **bool** |  | 
**two_way_link** | **bool** |  | 
**verified** | **bool** |  | 
**visibility** | **int** |  | 
**revoked** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.connected_account_response import ConnectedAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountResponse from a JSON string
connected_account_response_instance = ConnectedAccountResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountResponse.to_json())

# convert the object into a dict
connected_account_response_dict = connected_account_response_instance.to_dict()
# create an instance of ConnectedAccountResponse from a dict
connected_account_response_from_dict = ConnectedAccountResponse.from_dict(connected_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


