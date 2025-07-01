# PrivateChannelLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | **str** |  | 
**channel_id** | **str** |  | 

## Example

```python
from dc_rest.models.private_channel_location import PrivateChannelLocation

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateChannelLocation from a JSON string
private_channel_location_instance = PrivateChannelLocation.from_json(json)
# print the JSON string representation of the object
print(PrivateChannelLocation.to_json())

# convert the object into a dict
private_channel_location_dict = private_channel_location_instance.to_dict()
# create an instance of PrivateChannelLocation from a dict
private_channel_location_from_dict = PrivateChannelLocation.from_dict(private_channel_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


