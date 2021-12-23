# Protocol Documentation
<a name="top"/>

## Table of Contents
* [service_organization_id_lookup.proto](#service_organization_id_lookup.proto)
 * [OrganizationIdLookupService](#gittish.protocol.OrganizationIdLookupService)
* [Scalar Value Types](#scalar-value-types)

<a name="service_organization_id_lookup.proto"/>
<p align="right"><a href="#top">Top</a></p>

## service_organization_id_lookup.proto






<a name="gittish.protocol.OrganizationIdLookupService"/>
### OrganizationIdLookupService
Looks up the name or id of a given organization.

* Request

  `Reqres` of type `Reqres.Type.DATA`, assigned actor and an Operation for the data.
  The Operation needs to be of type OrganizationOperationType.Type.LOOKUP and
  the operation's data field needs to a NameId with either id or name filled in.
  The operation's id field can be left blank.

* Response

  On success, a Reqres of type Reqres.Type.DATA and a NameId for the data, or,
  on error, a Reqres of type Reqres.Type.EROR and an Error for the data.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| lookup | [Reqres](#gittish.protocol.Reqres) | [Reqres](#gittish.protocol.Reqres) |  |



<a name="scalar-value-types"/>
## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double"/> double |  | double | double | float |
| <a name="float"/> float |  | float | float | float |
| <a name="int32"/> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64"/> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32"/> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64"/> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32"/> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64"/> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32"/> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64"/> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32"/> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64"/> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool"/> bool |  | bool | boolean | boolean |
| <a name="string"/> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes"/> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |
