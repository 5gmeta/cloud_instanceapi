# Cloud Instance API
Source code and OpenAPI definitions

https://github.com/5gmeta/cloud_instanceapi/blob/main/api/cloudinstance-api/openapi_server/openapi/cloudinstance.yaml

## API

This API offers the following methods:

* GET /mecs/{mec_id}/types
	* GET all available instance types available in the mec and it's computing capabilities
		* CPU
		* RAM
		* GPU?

* POST /mecs/{mec_id}/types
	* Add a new instance type in a specific MEC
		* Set name
		* Set CPU
		* Set RAM
		* Set GPU

* GET /mecs/{mec_id}/types/{type_id}
	* GET certain instance type computing capabilities from a certain MEC

* DELETE /mecs/{mec_id}/types/{type_id}
	* Delete an instance type from a MEC


* GET /mecs/{mec_id}/instances
	* Returns deployed instances in a specific MEC

* POST /mecs/{mec_id}/instances
	* Deploys a instance in a specific MEC
		* Datatype
		* Username
		* Instance type

* GET /mecs/{mec_id}/instances/{instance_id}
	* Get information from a specific instance from a certain MEC

* DELETE /mecs/{mec_id}/instances/{instance_id}
	* Delete a deployed instance in a specific MEC


