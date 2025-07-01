# GithubAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from dc_rest.models.github_author import GithubAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of GithubAuthor from a JSON string
github_author_instance = GithubAuthor.from_json(json)
# print the JSON string representation of the object
print(GithubAuthor.to_json())

# convert the object into a dict
github_author_dict = github_author_instance.to_dict()
# create an instance of GithubAuthor from a dict
github_author_from_dict = GithubAuthor.from_dict(github_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


