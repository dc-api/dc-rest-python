# UserAvatarDecorationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | 
**sku_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.user_avatar_decoration_response import UserAvatarDecorationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserAvatarDecorationResponse from a JSON string
user_avatar_decoration_response_instance = UserAvatarDecorationResponse.from_json(json)
# print the JSON string representation of the object
print(UserAvatarDecorationResponse.to_json())

# convert the object into a dict
user_avatar_decoration_response_dict = user_avatar_decoration_response_instance.to_dict()
# create an instance of UserAvatarDecorationResponse from a dict
user_avatar_decoration_response_from_dict = UserAvatarDecorationResponse.from_dict(user_avatar_decoration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


