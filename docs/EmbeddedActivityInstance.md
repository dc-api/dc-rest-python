# EmbeddedActivityInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**instance_id** | **str** |  | 
**launch_id** | **str** |  | 
**location** | [**EmbeddedActivityInstanceLocation**](EmbeddedActivityInstanceLocation.md) |  | [optional] 
**users** | **List[str]** |  | 

## Example

```python
from dc_rest.models.embedded_activity_instance import EmbeddedActivityInstance

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedActivityInstance from a JSON string
embedded_activity_instance_instance = EmbeddedActivityInstance.from_json(json)
# print the JSON string representation of the object
print(EmbeddedActivityInstance.to_json())

# convert the object into a dict
embedded_activity_instance_dict = embedded_activity_instance_instance.to_dict()
# create an instance of EmbeddedActivityInstance from a dict
embedded_activity_instance_from_dict = EmbeddedActivityInstance.from_dict(embedded_activity_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


