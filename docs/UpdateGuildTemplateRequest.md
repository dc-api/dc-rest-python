# UpdateGuildTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_guild_template_request import UpdateGuildTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuildTemplateRequest from a JSON string
update_guild_template_request_instance = UpdateGuildTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuildTemplateRequest.to_json())

# convert the object into a dict
update_guild_template_request_dict = update_guild_template_request_instance.to_dict()
# create an instance of UpdateGuildTemplateRequest from a dict
update_guild_template_request_from_dict = UpdateGuildTemplateRequest.from_dict(update_guild_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


