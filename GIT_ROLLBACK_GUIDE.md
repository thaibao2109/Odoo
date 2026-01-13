# 🔄 Hướng dẫn quay lại commit gần nhất khi code lỗi

## 📋 Tổng quan

Khi code bị lỗi và cần quay lại commit trước đó, có nhiều cách tùy thuộc vào tình huống:

---

## 🎯 Cách 1: Xem lịch sử commit

Trước tiên, xem các commit gần đây:

```bash
cd /Users/baonguyen/Desktop/app/Odoo
git log --oneline -10
```

Kết quả sẽ hiển thị:
```
0c9db06 feat: Implement product attributes system with automatic SKU generation
...
```

---

## 🔙 Cách 2: Quay lại commit cụ thể (Soft Reset - Giữ thay đổi)

**Khi nào dùng:** Khi muốn quay lại commit trước nhưng vẫn giữ các thay đổi trong working directory (chưa commit)

```bash
# Xem commit hash
git log --oneline -5

# Quay lại commit trước đó (ví dụ: commit trước là abc1234)
git reset --soft HEAD~1

# Hoặc quay lại commit cụ thể
git reset --soft 0c9db06
```

**Lưu ý:**
- `--soft`: Giữ tất cả thay đổi trong staging area
- Có thể commit lại sau khi sửa lỗi

---

## 🔙 Cách 3: Quay lại commit cụ thể (Mixed Reset - Giữ file nhưng bỏ staging)

**Khi nào dùng:** Khi muốn quay lại và bỏ staging, nhưng vẫn giữ file trong working directory

```bash
# Quay lại 1 commit trước
git reset HEAD~1

# Hoặc quay lại commit cụ thể
git reset 0c9db06
```

**Lưu ý:**
- Thay đổi vẫn còn trong working directory
- Có thể sửa và commit lại

---

## 🔙 Cách 4: Quay lại commit cụ thể (Hard Reset - XÓA TẤT CẢ)

**⚠️ CẢNH BÁO:** Cách này sẽ XÓA TẤT CẢ thay đổi chưa commit!

**Khi nào dùng:** Khi chắc chắn muốn quay lại hoàn toàn và bỏ tất cả thay đổi hiện tại

```bash
# Quay lại 1 commit trước (XÓA TẤT CẢ thay đổi)
git reset --hard HEAD~1

# Hoặc quay lại commit cụ thể
git reset --hard 0c9db06
```

**Lưu ý:**
- `--hard`: XÓA TẤT CẢ thay đổi chưa commit
- Không thể khôi phục sau khi dùng `--hard`
- Chỉ dùng khi chắc chắn!

---

## 🔄 Cách 5: Tạo commit mới để revert (An toàn nhất)

**Khi nào dùng:** Khi đã push lên GitHub và muốn tạo commit mới để revert

```bash
# Xem commit cần revert
git log --oneline -5

# Revert commit gần nhất (tạo commit mới để undo)
git revert HEAD

# Hoặc revert commit cụ thể
git revert 0c9db06
```

**Lưu ý:**
- Tạo commit mới để undo commit cũ
- An toàn, không mất lịch sử
- Phù hợp khi đã push lên GitHub

---

## 📦 Cách 6: Quay lại và push lên GitHub

Sau khi quay lại commit, nếu muốn cập nhật GitHub:

```bash
# Quay lại commit (chọn một trong các cách trên)
git reset --hard 0c9db06

# Force push (CẨN THẬN! Chỉ dùng khi chắc chắn)
git push -f origin main
```

**⚠️ CẢNH BÁO:**
- `-f` (force push) sẽ ghi đè lịch sử trên GitHub
- Chỉ dùng khi làm việc một mình hoặc đã thông báo team

---

## 🛡️ Cách 7: Tạo branch backup trước khi rollback

**An toàn nhất:** Tạo branch backup trước khi rollback

```bash
# Tạo branch backup từ commit hiện tại
git branch backup-before-rollback

# Quay lại commit trước
git reset --hard HEAD~1

# Nếu cần khôi phục, chuyển về branch backup
git checkout backup-before-rollback
```

---

## 📝 Ví dụ thực tế

### Tình huống: Code bị lỗi sau khi commit

```bash
# Bước 1: Xem lịch sử
git log --oneline -5
# Output:
# abc1234 (HEAD) feat: New feature - BUGGY!
# 0c9db06 feat: Implement product attributes system
# ...

# Bước 2: Tạo backup (khuyến nghị)
git branch backup-abc1234

# Bước 3: Quay lại commit trước (0c9db06)
git reset --hard 0c9db06

# Bước 4: Kiểm tra code đã ổn chưa
# ... test code ...

# Bước 5: Nếu cần push lên GitHub
git push -f origin main
```

---

## 🔍 Kiểm tra trạng thái sau khi rollback

```bash
# Xem commit hiện tại
git log --oneline -3

# Xem trạng thái working directory
git status

# Xem các branch
git branch -a
```

---

## ⚠️ Lưu ý quan trọng

1. **Luôn tạo backup** trước khi rollback:
   ```bash
   git branch backup-$(date +%Y%m%d-%H%M%S)
   ```

2. **Nếu đã push lên GitHub:**
   - Dùng `git revert` thay vì `git reset --hard`
   - Hoặc dùng `git reset --hard` + `git push -f` (cẩn thận!)

3. **Nếu làm việc nhóm:**
   - Không dùng `git push -f` trừ khi đã thông báo
   - Dùng `git revert` để giữ lịch sử

4. **Khôi phục file đã xóa:**
   ```bash
   # Xem file đã xóa
   git log --diff-filter=D --summary
   
   # Khôi phục file từ commit trước
   git checkout HEAD~1 -- path/to/file
   ```

---

## 🆘 Khôi phục sau khi nhầm lẫn

Nếu đã dùng `git reset --hard` và muốn khôi phục:

```bash
# Xem reflog (lịch sử tất cả thao tác)
git reflog

# Khôi phục về commit trước khi reset
git reset --hard HEAD@{1}
```

---

## 📚 Tóm tắt các lệnh

| Lệnh | Mô tả | Khi nào dùng |
|------|-------|--------------|
| `git reset --soft HEAD~1` | Quay lại, giữ thay đổi trong staging | Muốn sửa và commit lại |
| `git reset HEAD~1` | Quay lại, giữ file nhưng bỏ staging | Muốn sửa file trước khi commit |
| `git reset --hard HEAD~1` | Quay lại, XÓA TẤT CẢ | Chắc chắn muốn quay lại hoàn toàn |
| `git revert HEAD` | Tạo commit mới để undo | Đã push lên GitHub, muốn an toàn |
| `git branch backup` | Tạo branch backup | Trước khi rollback (khuyến nghị) |

---

## ✅ Checklist trước khi rollback

- [ ] Đã xem lịch sử commit: `git log --oneline -10`
- [ ] Đã tạo branch backup: `git branch backup-xxx`
- [ ] Đã xác nhận commit cần quay lại
- [ ] Đã kiểm tra xem đã push lên GitHub chưa
- [ ] Đã thông báo team (nếu làm việc nhóm)

---

**💡 Tip:** Luôn dùng `git revert` thay vì `git reset --hard` khi đã push lên GitHub để giữ lịch sử và tránh conflict với team!
