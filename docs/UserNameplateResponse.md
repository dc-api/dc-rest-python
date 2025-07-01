# UserNameplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku_id** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**palette** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.user_nameplate_response import UserNameplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserNameplateResponse from a JSON string
user_nameplate_response_instance = UserNameplateResponse.from_json(json)
# print the JSON string representation of the object
print(UserNameplateResponse.to_json())

# convert the object into a dict
user_nameplate_response_dict = user_nameplate_response_instance.to_dict()
# create an instance of UserNameplateResponse from a dict
user_nameplate_response_from_dict = UserNameplateResponse.from_dict(user_nameplate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


