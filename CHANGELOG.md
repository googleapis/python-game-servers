# Changelog

### [1.2.1](https://www.github.com/googleapis/python-game-servers/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([c80d20e](https://www.github.com/googleapis/python-game-servers/commit/c80d20e0b3375be37533d29d9d708c694060a914))
* **deps:** require google-api-core >= 1.28.0 ([c80d20e](https://www.github.com/googleapis/python-game-servers/commit/c80d20e0b3375be37533d29d9d708c694060a914))


### Documentation

* list oneofs in docstring ([c80d20e](https://www.github.com/googleapis/python-game-servers/commit/c80d20e0b3375be37533d29d9d708c694060a914))

## [1.2.0](https://www.github.com/googleapis/python-game-servers/compare/v1.1.1...v1.2.0) (2021-10-26)


### Features

* add context manager support in client ([#202](https://www.github.com/googleapis/python-game-servers/issues/202)) ([2b0a6de](https://www.github.com/googleapis/python-game-servers/commit/2b0a6de4d7e74b567e4ada8bff88c5d74e9a36d6))


### Bug Fixes

* improper types in pagers generation ([5ea72d7](https://www.github.com/googleapis/python-game-servers/commit/5ea72d7efd2d84a1ed3454102ba6357111018489))

### [1.1.1](https://www.github.com/googleapis/python-game-servers/compare/v1.1.0...v1.1.1) (2021-09-27)


### Bug Fixes

* add 'dict' annotation type to 'request' ([3a701f7](https://www.github.com/googleapis/python-game-servers/commit/3a701f73fe732425d38b67e9c007113d1adc7d4d))


### Documentation

* **samples:** show cluster installation state details for get and list methods ([#188](https://www.github.com/googleapis/python-game-servers/issues/188)) ([e324a29](https://www.github.com/googleapis/python-game-servers/commit/e324a29030b4906f2704a2bae4000f854bb8bdc9))

## [1.1.0](https://www.github.com/googleapis/python-game-servers/compare/v1.0.2...v1.1.0) (2021-08-28)


### Features

* add cluster_state to show the state of the Kubernetes cluster ([a149bb7](https://www.github.com/googleapis/python-game-servers/commit/a149bb788248bd12dc905ff0d50becd557af0fb3))
* support version reporting API ([#180](https://www.github.com/googleapis/python-game-servers/issues/180)) ([a149bb7](https://www.github.com/googleapis/python-game-servers/commit/a149bb788248bd12dc905ff0d50becd557af0fb3))

### [1.0.2](https://www.github.com/googleapis/python-game-servers/compare/v1.0.1...v1.0.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#168](https://www.github.com/googleapis/python-game-servers/issues/168)) ([9d4ccd1](https://www.github.com/googleapis/python-game-servers/commit/9d4ccd1804824e5b3f9a3250d1c905c1f86e6d99))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#163](https://www.github.com/googleapis/python-game-servers/issues/163)) ([a4b018e](https://www.github.com/googleapis/python-game-servers/commit/a4b018e7dfd6c8cd8e084306a8fd21da5329c255))


### Miscellaneous Chores

* release as 1.0.2 ([#169](https://www.github.com/googleapis/python-game-servers/issues/169)) ([00c3a82](https://www.github.com/googleapis/python-game-servers/commit/00c3a824eee4a46f8b54172541c90afc542ee9f5))

### [1.0.1](https://www.github.com/googleapis/python-game-servers/compare/v1.0.0...v1.0.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#162](https://www.github.com/googleapis/python-game-servers/issues/162)) ([a4263ce](https://www.github.com/googleapis/python-game-servers/commit/a4263ce7550cf34f96875ed7bf01e825d2211911))

## [1.0.0](https://www.github.com/googleapis/python-game-servers/compare/v0.5.0...v1.0.0) (2021-06-30)


### Features

* bump release level to production/stable ([#120](https://www.github.com/googleapis/python-game-servers/issues/120)) ([7abb7bb](https://www.github.com/googleapis/python-game-servers/commit/7abb7bb281c9cd1bbd94a9aa08690f6ed2faf349))

## [0.5.0](https://www.github.com/googleapis/python-game-servers/compare/v0.4.2...v0.5.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#137](https://www.github.com/googleapis/python-game-servers/issues/137)) ([e0e5c5f](https://www.github.com/googleapis/python-game-servers/commit/e0e5c5fc643c28df4b6a199642b271a710c0c047))


### Bug Fixes

* disable always_use_jwt_access ([#141](https://www.github.com/googleapis/python-game-servers/issues/141)) ([3867cdf](https://www.github.com/googleapis/python-game-servers/commit/3867cdf2bf956f84371ffbaa558a444c1f699564))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-game-servers/issues/1127)) ([#132](https://www.github.com/googleapis/python-game-servers/issues/132)) ([46c7313](https://www.github.com/googleapis/python-game-servers/commit/46c7313ab392d08b956793fbb9babc2e2e13091a)), closes [#1126](https://www.github.com/googleapis/python-game-servers/issues/1126)

### [0.4.2](https://www.github.com/googleapis/python-game-servers/compare/v0.4.1...v0.4.2) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#128](https://www.github.com/googleapis/python-game-servers/issues/128)) ([624542d](https://www.github.com/googleapis/python-game-servers/commit/624542d4251575629172b473ff1e9215e6c982c0))

### [0.4.1](https://www.github.com/googleapis/python-game-servers/compare/v0.4.0...v0.4.1) (2021-05-28)


### Bug Fixes

* **deps:** add packaging requirement ([#122](https://www.github.com/googleapis/python-game-servers/issues/122)) ([af6460a](https://www.github.com/googleapis/python-game-servers/commit/af6460a38fa0cd5d6aebec02152ca49f9a91bf0d))

## [0.4.0](https://www.github.com/googleapis/python-game-servers/compare/v0.3.0...v0.4.0) (2021-05-16)


### Features

* add `from_service_account_info` ([#90](https://www.github.com/googleapis/python-game-servers/issues/90)) ([f1ce240](https://www.github.com/googleapis/python-game-servers/commit/f1ce24029d7b963a7a5c7eb459cea59a2a4ecaaf))
* add common resource path helper methods, expose client transport ([#45](https://www.github.com/googleapis/python-game-servers/issues/45)) ([cf0999f](https://www.github.com/googleapis/python-game-servers/commit/cf0999fd3a95b77ef32977318019193a777d4c5b))


### Bug Fixes

* fix retry deadlines ([f1ce240](https://www.github.com/googleapis/python-game-servers/commit/f1ce24029d7b963a7a5c7eb459cea59a2a4ecaaf))
* remove gRPC send/recv limit; expose client transport ([#71](https://www.github.com/googleapis/python-game-servers/issues/71)) ([79622f7](https://www.github.com/googleapis/python-game-servers/commit/79622f71f807c5c09d88c757e51794813cda5572))

## [0.3.0](https://www.github.com/googleapis/python-game-servers/compare/v0.2.0...v0.3.0) (2020-08-07)


### Features

* add v1 ([#36](https://www.github.com/googleapis/python-game-servers/issues/36)) ([db5d764](https://www.github.com/googleapis/python-game-servers/commit/db5d76495aa7410934651847d0d97de17b5a747d))


### Documentation

* **samples:** add samples for game server deployments ([#25](https://www.github.com/googleapis/python-game-servers/issues/25)) ([a3dee35](https://www.github.com/googleapis/python-game-servers/commit/a3dee35ff4db631a6f28c2b46e46e3fa66ba9418))
* add more code samples for game servers ([#32](https://www.github.com/googleapis/python-game-servers/issues/32)) ([2d30003](https://www.github.com/googleapis/python-game-servers/commit/2d300031213fda468b6aa52d3ee8635215c37986))

## [0.2.0](https://www.github.com/googleapis/python-game-servers/compare/v0.1.1...v0.2.0) (2020-07-13)


### Features

* add async support ([#20](https://www.github.com/googleapis/python-game-servers/issues/20)) ([952f47e](https://www.github.com/googleapis/python-game-servers/commit/952f47e2094c0246953ae537add751fe0159710b))
* add mtls support and resource path parse methods ([#10](https://www.github.com/googleapis/python-game-servers/issues/10)) ([dabeec7](https://www.github.com/googleapis/python-game-servers/commit/dabeec79e08c52e1616e890cb3b39aac729da115))
* add resource path parse methods ([#13](https://www.github.com/googleapis/python-game-servers/issues/13)) ([1b85e6c](https://www.github.com/googleapis/python-game-servers/commit/1b85e6c6523fc588f235fd9e320238101c63fade))


### Documentation

* add multiprocessing ([#11](https://www.github.com/googleapis/python-game-servers/issues/11)) ([3528a72](https://www.github.com/googleapis/python-game-servers/commit/3528a72c887b51b2dd0484869d028ed8f98c8c79))

### [0.1.1](https://www.github.com/googleapis/python-game-servers/compare/v0.1.0...v0.1.1) (2020-03-23)


### Bug Fixes

* correct package name ([#4](https://www.github.com/googleapis/python-game-servers/issues/4)) ([22d4bb0](https://www.github.com/googleapis/python-game-servers/commit/22d4bb05cd072beb63f5c00edbabd3642dd15bb8))

## 0.1.0 (2020-03-23)


### Features

* generate v1beta ([c888fb7](https://www.github.com/googleapis/python-game-servers/commit/c888fb7dd6c5d57ee4709624ab88b8fe2fd4286f))
