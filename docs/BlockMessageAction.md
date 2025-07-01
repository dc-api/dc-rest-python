# BlockMessageAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**BlockMessageActionMetadata**](BlockMessageActionMetadata.md) |  | [optional] 

## Example

```python
from dc_rest.models.block_message_action import BlockMessageAction

# TODO update the JSON string below
json = "{}"
# create an instance of BlockMessageAction from a JSON string
block_message_action_instance = BlockMessageAction.from_json(json)
# print the JSON string representation of the object
print(BlockMessageAction.to_json())

# convert the object into a dict
block_message_action_dict = block_message_action_instance.to_dict()
# create an instance of BlockMessageAction from a dict
block_message_action_from_dict = BlockMessageAction.from_dict(block_message_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


