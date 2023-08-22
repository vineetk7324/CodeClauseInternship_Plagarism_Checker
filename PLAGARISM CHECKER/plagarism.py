import difflib

def calculate_similarity(text1, text2):
    seq_matcher = difflib.SequenceMatcher(None, text1, text2)
    similarity_ratio = seq_matcher.ratio()
    return similarity_ratio

def check_plagiarism(file_path1, file_path2, threshold=0.8):
    with open(file_path1, 'r', encoding='utf-8') as file1, open(file_path2, 'r', encoding='utf-8') as file2:
        content1 = file1.read()
        content2 = file2.read()
        
        similarity = calculate_similarity(content1, content2)
        
        if similarity >= threshold:
            print("Plagiarism detected!")
            print(f"Similarity ratio: {similarity:.2f}")
        else:
            print("No plagiarism detected.")
            print(f"Similarity ratio: {similarity:.2f}")

if __name__ == "__main__":
    file_path1 = "document1.txt"
    file_path2 = "document2.txt"
    threshold = 0.8
    
    check_plagiarism(file_path1, file_path2, threshold)
