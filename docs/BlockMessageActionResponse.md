# BlockMessageActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**BlockMessageActionMetadataResponse**](BlockMessageActionMetadataResponse.md) |  | 

## Example

```python
from dc_rest.models.block_message_action_response import BlockMessageActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlockMessageActionResponse from a JSON string
block_message_action_response_instance = BlockMessageActionResponse.from_json(json)
# print the JSON string representation of the object
print(BlockMessageActionResponse.to_json())

# convert the object into a dict
block_message_action_response_dict = block_message_action_response_instance.to_dict()
# create an instance of BlockMessageActionResponse from a dict
block_message_action_response_from_dict = BlockMessageActionResponse.from_dict(block_message_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


