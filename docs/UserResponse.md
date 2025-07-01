# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**avatar** | **str** |  | [optional] 
**discriminator** | **str** |  | 
**public_flags** | **int** |  | 
**flags** | **int** |  | 
**bot** | **bool** |  | [optional] 
**system** | **bool** |  | [optional] 
**banner** | **str** |  | [optional] 
**accent_color** | **int** |  | [optional] 
**global_name** | **str** |  | [optional] 
**avatar_decoration_data** | [**UserAvatarDecorationResponse**](UserAvatarDecorationResponse.md) |  | [optional] 
**collectibles** | [**UserCollectiblesResponse**](UserCollectiblesResponse.md) |  | [optional] 
**primary_guild** | [**UserPrimaryGuildResponse**](UserPrimaryGuildResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


