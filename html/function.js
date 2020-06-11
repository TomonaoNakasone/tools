function splitSpace($baseString) {
	return $baseString.split(' ');
}
function getString($splitedData, $index, $byteNum) {
	return $splitedData.slice($index, $byteNum).join(" ");
}

$(function() {
	// クリックイベント
	$("#execute_btn").on("click", function() {
		var $baseText = $("#base_text").val();
		var $splitedData = splitSpace($baseText);
		var $resultData = new Array();

		var $index = 0;
		$resultData.push(getString($splitedData, $index, 5));
		$index = $index + 5;
		
		// あまりのデータを格納
		$resultData.push(getString($splitedData, $index, $splitedData.length));
		
		// 改行で区切って連結したものを結果に格納
		$("#result_1").val($resultData.join("\n"));
		alert("処理が終了しました");
	});
});
