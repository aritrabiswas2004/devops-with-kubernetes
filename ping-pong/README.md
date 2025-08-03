# Ping-Pong Application

This is the ping pong application in the `exercises` namespace in my cluster.

## Deployment

The following can be created by `kubectl apply -f manifests/`

- StatefulSet (and related Service)
- Deployment
- Service

> It is highly recommended that StatefulSet is applied first and `postgres` pods are up **AND RUNNING WITHOUT ERRORS** by executing `kubectl apply -f manifests/statefulset.yaml`. This is to avoid `CrashLoopBackOff` errors that occur on pods dependent on the statefulset when deployed to GKE. 

## Volumes

For the exercises that required a PV and PVC, it can be created with `kubectl apply -f volumes/`

> In case of exercises working on GKE, `persistentvolume.yaml` file in completely commented since GKE dynamically provisions persistent disks.

