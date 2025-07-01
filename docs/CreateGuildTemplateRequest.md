# CreateGuildTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.create_guild_template_request import CreateGuildTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildTemplateRequest from a JSON string
create_guild_template_request_instance = CreateGuildTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGuildTemplateRequest.to_json())

# convert the object into a dict
create_guild_template_request_dict = create_guild_template_request_instance.to_dict()
# create an instance of CreateGuildTemplateRequest from a dict
create_guild_template_request_from_dict = CreateGuildTemplateRequest.from_dict(create_guild_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


