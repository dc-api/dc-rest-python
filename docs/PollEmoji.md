# PollEmoji


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**animated** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.poll_emoji import PollEmoji

# TODO update the JSON string below
json = "{}"
# create an instance of PollEmoji from a JSON string
poll_emoji_instance = PollEmoji.from_json(json)
# print the JSON string representation of the object
print(PollEmoji.to_json())

# convert the object into a dict
poll_emoji_dict = poll_emoji_instance.to_dict()
# create an instance of PollEmoji from a dict
poll_emoji_from_dict = PollEmoji.from_dict(poll_emoji_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


