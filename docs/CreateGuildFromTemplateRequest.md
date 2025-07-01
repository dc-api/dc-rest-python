# CreateGuildFromTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**icon** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.create_guild_from_template_request import CreateGuildFromTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildFromTemplateRequest from a JSON string
create_guild_from_template_request_instance = CreateGuildFromTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGuildFromTemplateRequest.to_json())

# convert the object into a dict
create_guild_from_template_request_dict = create_guild_from_template_request_instance.to_dict()
# create an instance of CreateGuildFromTemplateRequest from a dict
create_guild_from_template_request_from_dict = CreateGuildFromTemplateRequest.from_dict(create_guild_from_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


