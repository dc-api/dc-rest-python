# EmbeddedActivityInstanceLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | **str** |  | 
**channel_id** | **str** |  | 
**guild_id** | **str** |  | 

## Example

```python
from dc_rest.models.embedded_activity_instance_location import EmbeddedActivityInstanceLocation

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedActivityInstanceLocation from a JSON string
embedded_activity_instance_location_instance = EmbeddedActivityInstanceLocation.from_json(json)
# print the JSON string representation of the object
print(EmbeddedActivityInstanceLocation.to_json())

# convert the object into a dict
embedded_activity_instance_location_dict = embedded_activity_instance_location_instance.to_dict()
# create an instance of EmbeddedActivityInstanceLocation from a dict
embedded_activity_instance_location_from_dict = EmbeddedActivityInstanceLocation.from_dict(embedded_activity_instance_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


