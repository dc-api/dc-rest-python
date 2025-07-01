# UserCollectiblesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameplate** | [**UserNameplateResponse**](UserNameplateResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.user_collectibles_response import UserCollectiblesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectiblesResponse from a JSON string
user_collectibles_response_instance = UserCollectiblesResponse.from_json(json)
# print the JSON string representation of the object
print(UserCollectiblesResponse.to_json())

# convert the object into a dict
user_collectibles_response_dict = user_collectibles_response_instance.to_dict()
# create an instance of UserCollectiblesResponse from a dict
user_collectibles_response_from_dict = UserCollectiblesResponse.from_dict(user_collectibles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


