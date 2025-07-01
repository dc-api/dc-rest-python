# InteractionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**response_message_id** | **str** |  | [optional] 
**response_message_loading** | **bool** |  | [optional] 
**response_message_ephemeral** | **bool** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**guild_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.interaction_response import InteractionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionResponse from a JSON string
interaction_response_instance = InteractionResponse.from_json(json)
# print the JSON string representation of the object
print(InteractionResponse.to_json())

# convert the object into a dict
interaction_response_dict = interaction_response_instance.to_dict()
# create an instance of InteractionResponse from a dict
interaction_response_from_dict = InteractionResponse.from_dict(interaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


