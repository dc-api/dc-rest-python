# InnerErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | The list of errors for this field | 

## Example

```python
from dc_rest.models.inner_errors import InnerErrors

# TODO update the JSON string below
json = "{}"
# create an instance of InnerErrors from a JSON string
inner_errors_instance = InnerErrors.from_json(json)
# print the JSON string representation of the object
print(InnerErrors.to_json())

# convert the object into a dict
inner_errors_dict = inner_errors_instance.to_dict()
# create an instance of InnerErrors from a dict
inner_errors_from_dict = InnerErrors.from_dict(inner_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


