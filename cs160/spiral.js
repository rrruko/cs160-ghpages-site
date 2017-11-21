window.onload = function() {
    let img = new Image();
    let canvas = document.getElementById("canvas");
    const fileInput = document.getElementById("file-input");
    const maxScale = document.getElementById("max-scale");
    fileInput.addEventListener("change", handleFile);
    maxScale.addEventListener("change", handleScale);

    function handleFile(e) {
        if (!maxScale.value) {
            return;
        }
        img.src = URL.createObjectURL(e.target.files[0]);
        img.onload = function() {
            spiral(1, parseInt(maxScale.value), img);
        };
    }

    function handleScale(e) {
        if (img) {
            spiral(1, parseInt(maxScale.value), img);
        }
    }

    // This is just a needlessly complex, ad-hoc logarithmic spiral implementation
    // The `draw` function will render log2(endScale) copies of the supplied image
    // in a spiral formation.
    function spiral(startScale, endScale, img) {
        if (!img || img.width == 0) {
            console.log("no image found");
            return;
        }
        if ([1, 2, 4, 8, 16].indexOf(endScale) === -1) {
            console.log("endScale isn't a multiple of 2");
            return;
        }

        endScale = Math.round(endScale);

        let imgData = getData(img);

        let w = img.width;
        let h = img.height;

        canvas.width = 3 / 2 * w * endScale;
        canvas.height = h * endScale;
        let cnvs = canvas.getContext("2d");

        let direction = 0;
        let middleX = w * endScale / 2;
        let middleY = h * endScale / 2;

        let sin = Math.sin;
        let cos = Math.cos;
        for (let i = endScale; i >= startScale; i /= 2) {
            let widthI = w * i;
            let heightI = h * i;
            let x = middleX - widthI / 2;
            let y = middleY - heightI / 2;

            const scaled = ImageFilters.ResizeNearestNeighbor(imgData, widthI, heightI);
            cnvs.putImageData(scaled, x, y);

            middleX += cos(direction)               * 0.75 * widthI
                     + cos(direction - Math.PI / 2) * 0.25 * widthI;

            middleY += sin(direction)               * 0.75 * heightI
                     + sin(direction - Math.PI / 2) * 0.25 * heightI;

            direction += Math.PI / 2;
        }
    }

    function getData(img) {
        var canvas = document.createElement("canvas");
        var context = canvas.getContext("2d");
        canvas.width = img.width;
        canvas.height = img.height;
        context.drawImage(img, 0, 0);
        return context.getImageData(0, 0, img.width, img.height);
    }
}
