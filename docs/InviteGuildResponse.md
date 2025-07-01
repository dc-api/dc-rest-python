# InviteGuildResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**splash** | **str** |  | [optional] 
**banner** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**features** | **List[str]** |  | 
**verification_level** | **int** |  | [optional] 
**vanity_url_code** | **str** |  | [optional] 
**nsfw_level** | **int** |  | [optional] 
**nsfw** | **bool** |  | [optional] 
**premium_subscription_count** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.invite_guild_response import InviteGuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InviteGuildResponse from a JSON string
invite_guild_response_instance = InviteGuildResponse.from_json(json)
# print the JSON string representation of the object
print(InviteGuildResponse.to_json())

# convert the object into a dict
invite_guild_response_dict = invite_guild_response_instance.to_dict()
# create an instance of InviteGuildResponse from a dict
invite_guild_response_from_dict = InviteGuildResponse.from_dict(invite_guild_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


