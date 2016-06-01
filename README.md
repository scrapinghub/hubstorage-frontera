HCF (HubStorage Frontier) Backend for Frontera
==============================================

This package contains a common Hubstorage backend, queue and states components for Frontera. 

Main features
-------------
 - States are implemented using collections.
 - Distributed Backend run mode isn't supported yet (but Distributed Spiders is).
 - Using memory cache to store states.
 - HCFQueue and HCFStates classes can be used as building blocks to arrange any kind of crawling logic.
