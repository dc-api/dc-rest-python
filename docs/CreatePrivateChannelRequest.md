# CreatePrivateChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** |  | [optional] 
**access_tokens** | **List[str]** |  | [optional] 
**nicks** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from dc_rest.models.create_private_channel_request import CreatePrivateChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrivateChannelRequest from a JSON string
create_private_channel_request_instance = CreatePrivateChannelRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePrivateChannelRequest.to_json())

# convert the object into a dict
create_private_channel_request_dict = create_private_channel_request_instance.to_dict()
# create an instance of CreatePrivateChannelRequest from a dict
create_private_channel_request_from_dict = CreatePrivateChannelRequest.from_dict(create_private_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


