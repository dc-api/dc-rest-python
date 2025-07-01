# ApplicationFormPartialDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | 
**localizations** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dc_rest.models.application_form_partial_description import ApplicationFormPartialDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFormPartialDescription from a JSON string
application_form_partial_description_instance = ApplicationFormPartialDescription.from_json(json)
# print the JSON string representation of the object
print(ApplicationFormPartialDescription.to_json())

# convert the object into a dict
application_form_partial_description_dict = application_form_partial_description_instance.to_dict()
# create an instance of ApplicationFormPartialDescription from a dict
application_form_partial_description_from_dict = ApplicationFormPartialDescription.from_dict(application_form_partial_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


