package test;

public class PatternMatching {
	private String text;
	boolean[][] matrix;

	public PatternMatching(String text) {
		this.text = text;
	}

	public boolean checkPattern(String pattern) {
		matrix = new boolean[text.length() + 1][pattern.length() + 1];
		int i = 0;
		while (i < pattern.length() && (pattern.charAt(i) == '?' || pattern.charAt(i) == '*'))
			matrix[0][++i] = true;
		matrix[0][0] = true;
		// For each letter in the text
		for (int str = 1; str < text.length() + 1; str++) {
			printsTable();
			// For each letter in the pattern
			for (int pat = 1; pat < pattern.length() + 1; pat++) {
				if (text.charAt(str - 1) == pattern.charAt(pat - 1)) {
					if (matrix[str - 1][pat - 1])
						matrix[str][pat] = true;
				} else if (pattern.charAt(pat - 1) == '?') {
					if (matrix[str - 1][pat - 1])
						matrix[str][pat] = true;
					if (matrix[str][pat - 1])
						matrix[str][pat] = true;
				} else if (pattern.charAt(pat - 1) == '*') {
					if (matrix[str - 1][pat - 1])
						matrix[str][pat] = true;
					if (matrix[str][pat - 1])
						matrix[str][pat] = true;
					if (matrix[str - 1][pat])
						matrix[str][pat] = true;
				}
			}
		}
		return matrix[matrix.length - 1][matrix[0].length - 1];
	}

	public void printsTable() {
		for(int i = 0; i < matrix.length; i++) {
			System.out.print("[" + matrix[i][0]);
			for(int j = 1; j < matrix[0].length; j++) {
				System.out.print(";" + matrix[i][j]);
			}
			System.out.println("]");
		}
		System.out.println("---------------------------------------");
	}
}
