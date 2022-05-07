if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register("/service_worker.js", {
        scope: "/",
    });
}
// Get the server's public key
const public_Key = "BPz498JcmPRt-UCDJkCNpPBI-kheVTHJopcz3AHRM5utKOCI3L07Z3xr1rwSqAK3NVN-rcLzuchSAqcIvHpcDIE";

// Copied from the web-push documentation 
const urlBase64ToUint8Array = (base64String) => {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
};

window.subscribe = async () => {
    if (!("serviceWorker" in navigator)) return;
  
    const registration = await navigator.serviceWorker.ready;
  
    const subscription = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array(public_Key),
    });

    fetch("/api/subscribe", {
        method: "POST",
        body: JSON.stringify({
            subscription_json: JSON.stringify(subscription),
        }),
        headers: {
            "content-type": "application/json",
        },
    });
};

window.broadcast = async () => {
    await fetch("/api/broadcast", {
        method: "GET",
        headers: {
            "content-type": "application/json",
        },
    });
};