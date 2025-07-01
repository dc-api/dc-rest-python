# PollMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**emoji** | [**PollEmoji**](PollEmoji.md) |  | [optional] 

## Example

```python
from dc_rest.models.poll_media import PollMedia

# TODO update the JSON string below
json = "{}"
# create an instance of PollMedia from a JSON string
poll_media_instance = PollMedia.from_json(json)
# print the JSON string representation of the object
print(PollMedia.to_json())

# convert the object into a dict
poll_media_dict = poll_media_instance.to_dict()
# create an instance of PollMedia from a dict
poll_media_from_dict = PollMedia.from_dict(poll_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


